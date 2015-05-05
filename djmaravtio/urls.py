from django.conf.urls import include, url
from django.contrib import admin
from products.models import TequilaType, EventType, BoxPresentation, Template
from rest_framework import routers, serializers, viewsets
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
        fields = ('id', 'bottlesize', 'bottles', 'maxlabels', 'bottlerow')


class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = TequilaType.objects.all()
    serializer_class = TequilaTypeSerializer



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = BoxPresentation.objects.all()
    serializer_class = BoxPresentationSerializer


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

primary_router = drf_routers.SimpleRouter()
primary_router.register(r'events', EventTypeViewSet)

secondary_router = drf_routers.NestedSimpleRouter(primary_router, r'events', lookup='event')
secondary_router.register(r'templates', TemplateViewSet)


router = routers.DefaultRouter()
router.register('tequila', TequilaTypeViewSet)
#router.register('events', EventTypeViewSet)
router.register('details', BoxPresentationViewSet)
router.register('templates', TemplateViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'djmaravtio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(primary_router.urls)),
    url(r'^api/', include(secondary_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

