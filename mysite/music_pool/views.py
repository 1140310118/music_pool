from django.shortcuts import render
from django.db import transaction

# Create your views here.

from music_pool.models import Song

@transaction.atomic
def all_song(request):
	try:
		with transaction.atomic():
			sfs_list=Song.get_all()
	except IntegrityError:
		sfs_list=[]
	context = {'sfs_list': sfs_list}
	return render(request, 'music_pool/index.html', context)