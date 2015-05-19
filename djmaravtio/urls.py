from django.conf.urls import include, url
from django.contrib import admin
from products.models import TequilaType, EventType, BoxPresentation, Template, CustomImage
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework_nested import routers as drf_routers

from django.conf import settings
from django.conf.urls.static import static

class TequilaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TequilaType
        fields = ('id', 'name', 'bimage', 'maskimage',)


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'etype', 'timage',)


class EventTypeSerializer(serializers.ModelSerializer):
    #templates = TemplateSerializer(many=True, read_only=True)

    class Meta:
        model = EventType
        fields = ('id', 'name',)# 'templates',)


class BoxPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxPresentation
        fields = ('id', 'type', 'bottlesize', 'bottles',
                  'maxlabels', 'bottlerow', 'img_original_size',
                  'img_zoom_size', 'img_tag'
        )


class CustomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomImage
        fields = ('id', 'file', 'name')


class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = TequilaType.objects.all()
    serializer_class = TequilaTypeSerializer



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = BoxPresentation.objects.all()
    serializer_class = BoxPresentationSerializer

    def list(self, request, size_pk=None, *args, **kwargs):
        if size_pk:
            queryset = self.queryset.filter(type_id=size_pk)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def list(self, request, event_pk=None, *args, **kwargs):
        if event_pk:
            queryset = self.queryset.filter(etype=event_pk)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CustomImageViewSet(viewsets.ModelViewSet):
    queryset = CustomImage.objects.all()
    serializer_class = CustomImageSerializer

    def create(self, request, *args, **kwargs):
        print 'Request Data:'
        print request.data
        serializer = self.get_serializer(data=request.data)

        ser = serializer.is_valid(raise_exception=True)
        print 'Serializer:'
        #print serializer.data
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

primary_router = drf_routers.SimpleRouter()
primary_router.register(r'events', EventTypeViewSet)
primary_router.register(r'types', TequilaTypeViewSet)

secondary_router_events = drf_routers.NestedSimpleRouter(primary_router, r'events', lookup='event')
secondary_router_events.register(r'templates', TemplateViewSet)
secondary_router_types = drf_routers.NestedSimpleRouter(primary_router, r'types', lookup='size')
secondary_router_types.register(r'sizes', BoxPresentationViewSet)


router = routers.DefaultRouter()
router.register('types', TequilaTypeViewSet)
router.register('events', EventTypeViewSet)
router.register('sizes', BoxPresentationViewSet)
router.register('templates', TemplateViewSet)
router.register('customimages', CustomImageViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'djmaravtio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(primary_router.urls)),
    url(r'^api/', include(secondary_router_events.urls)),
    url(r'^api/', include(secondary_router_types.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

