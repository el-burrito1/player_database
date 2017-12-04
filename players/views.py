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
				queryset = Player.objects.filter(height__gte=6020,weight__gte=215,position='QB')
			elif selection == 'WR':
					queryset = Player.objects.filter(height__gte=5110,weight__gte=185,position='WR')
			elif selection == 'FB':
					queryset = Player.objects.filter(height__gte=6000,weight__gte=240,position='FB')
			elif selection == 'RB':
					queryset = Player.objects.filter(height__gte=5010,weight__gte=215,position='RB')
			elif selection == 'TE':
					queryset = Player.objects.filter(height__gte=6030,weight__gte=250,position='TE')
			elif selection == 'OT':
					queryset = Player.objects.filter(height__gte=6050,weight__gte=300,position='OT')
			elif selection == 'OG':
					queryset = Player.objects.filter(height__gte=6030,weight__gte=300,position='OG')
			elif selection == 'C':
					queryset = Player.objects.filter(height__gte=6030,weight__gte=290,position='C')
			elif selection == 'S':
					queryset = Player.objects.filter(height__gte=5010,weight__gte=195,position='S')
			elif selection == 'CB':
					queryset = Player.objects.filter(height__gte=5010,weight__gte=185,position='CB')
			elif selection == 'ILB':
					queryset = Player.objects.filter(height__gte=6000,weight__gte=235,position='ILB')
			elif selection == 'OLB':
					queryset = Player.objects.filter(height__gte=6020,weight__gte=230,position='OLB')
			elif selection == 'DE':
					queryset = Player.objects.filter(height__gte=6030,weight__gte=255,position='DE')
			elif selection == 'DT':
					queryset = Player.objects.filter(height__gte=6020,weight__gte=295,position='DT')
			elif selection == 'LS':
					queryset = Player.objects.filter(height__gte=6020,weight__gte=250,position='LS')
			elif selection == 'P':
					queryset = Player.objects.filter(height__gte=6020,weight__gte=190,position='P')
			elif selection == 'K':
					queryset = Player.objects.filter(height__gte=5010,weight__gte=180,position='K')
			return queryset
		else:
			return queryset
