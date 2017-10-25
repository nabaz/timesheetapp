from rest_framework import serializers
from api.models.customer import Customer


class CustomerSerializer(serializers.Serializer):
    STATUS = (
        ('A', 'Active'),
        ('IA', 'InActive'),
        ('C', 'Closed'),
    )

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField()
    phone = serializers.CharField(required=False)
    note = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS)

    class Meta:
        model = Customer

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass
        # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # """
        # instance.title = validated_data.get('title', instance.title)
        # instance.code = validated_data.get('code', instance.code)
        # instance.linenos = validated_data.get('linenos', instance.linenos)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        # instance.save()
        # return instance
