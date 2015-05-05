from django.conf.urls import include, url
from django.contrib import admin
from products.models import TequilaType, EventType, BoxPresentation, Template
from rest_framework import routers, serializers, viewsets

class TequilaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TequilaType
        fields = ('id', 'name',)

class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = TequilaType.objects.all()
    serializer_class = TequilaTypeSerializer

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'name',)

class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class BoxPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxPresentation
        fields = ('id', 'bottlesize', 'bottles', 'maxlabels',)

class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = BoxPresentation.objects.all()
    serializer_class = BoxPresentationSerializer


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'etype', 'timage',)

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


router = routers.DefaultRouter()
router.register('teqtype', TequilaTypeViewSet)
router.register('evtype', EventTypeViewSet)
router.register('boxp', BoxPresentationViewSet)
router.register('template', TemplateViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'djmaravtio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
