from rest_framework_mongoengine import viewsets as meviewsets

from crmsystem.models import Employee
from crmsystem.serializers import EmployeeSerializer


class EmployeeView(meviewsets.ModelViewSet):
    lookup_field = 'employeeId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


