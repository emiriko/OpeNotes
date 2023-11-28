from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from report.models import Laporan
from report.serializers import LaporanSerializer
from django.contrib.auth.models import User
from notes.models import Notes

class LaporanManager(APIView):
    permission_classes = []
    def get(self, request):
        self.permission_classes = [IsAdminUser]
        laporan_not_reviewed = Laporan.objects.filter(reviewed=False)

        return render(request, "report_list.html", {"list_laporan": laporan_not_reviewed})
    
    def post(self, request):
        notes_id = request.data['notes_id']
        notes = Notes.objects.get(id=notes_id)
        alasan = request.data['alasan']

        laporan = Laporan(pelapor=request.user, terlapor=notes, alasan=alasan)
        laporan.save()

        return Response(request.data, status=status.HTTP_201_CREATED)

class LaporanDetailView(APIView):
    permission_classes = []
    def get(self, request, id):
        self.permission_classes = [IsAdminUser]
        laporan = Laporan.objects.get(id=id)

        return render(request, "laporan_detail.html", {"laporan": laporan})

class LaporanValid(APIView):
    permission_classes = []
    def get(self, request, id):
        self.permission_classes = [IsAdminUser]

        laporan = Laporan.objects.get(id=id)
        laporan.reviewed = True
        laporan.save()

        laporan.terlapor.delete()

        return render(request, "report_list.html", {"laporan": laporan})

class LaporanInvalid(APIView):
    permission_classes = []
    def get(self, request, id):
        self.permission_classes = [IsAdminUser]

        laporan = Laporan.objects.get(id=id)
        laporan.reviewed = True
        laporan.save()

        return redirect("report_list")