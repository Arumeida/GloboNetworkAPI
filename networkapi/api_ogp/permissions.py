# -*- coding:utf-8 -*-
from rest_framework.permissions import BasePermission

from networkapi.admin_permission import AdminPermission
from networkapi.auth import has_perm


class Read(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.USER_ADMINISTRATION,
            AdminPermission.READ_OPERATION
        )


class Write(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.USER_ADMINISTRATION,
            AdminPermission.WRITE_OPERATION
        )
