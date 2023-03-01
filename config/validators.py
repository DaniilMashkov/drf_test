from rest_framework import serializers


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'youtube.com' not in value.get('link'):
            raise serializers.ValidationError('link must include "youtube.com"')
