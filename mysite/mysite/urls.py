from django.conf.urls import include, url, patterns
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^music_pool/', include('music_pool.urls')),
    url(r'^admin/', include(admin.site.urls)),
)