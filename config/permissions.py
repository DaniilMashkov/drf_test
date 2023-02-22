from rest_framework import permissions


class ModeratorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.has_perms(
                (
                        'courses.view_course',
                        'courses.change_course',
                        'lessons.view_lesson',
                        'lessons.change_lesson'
                ),
        ): return True


class ProfilePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.email == view.get_object().email:
            return True
