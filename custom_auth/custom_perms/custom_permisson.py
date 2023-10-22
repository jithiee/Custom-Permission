from rest_framework.permissions import BasePermission

class Mypermissions(BasePermission):
      def has_permission(self,request,view):
          if request.method == 'GET':
        #   if request.method == 'POST':
              return True
          return False
      
           