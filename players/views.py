# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from players.models import Player

# Create your views here.
class PlayerList(ListView):
	model = Player
	# queryset = Player.objects.filter(weight__gt=195,weight__lt=220)
	
	template_name = 'rosters/player_list.html'
	def get_queryset(self):
		queryset = Player.objects.all()
		if self.request.GET.get('position'):
			selection = self.request.GET.get('position')
			if selection == 'QB':
				queryset = Player.objects.filter(weight__gt=195,weight__lt=220,position='QB')
			elif selection == 'WR':
					queryset = Player.objects.filter(position='WR')
			elif selection == 'DB':
					queryset = Player.objects.filter(position='DB')
			return queryset
		else:
			return queryset
