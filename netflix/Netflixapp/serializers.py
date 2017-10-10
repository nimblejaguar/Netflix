from rest_framework import serializers
from .models import Netflix, Payment,contact,Movies,Genre


class NetflixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Netflix
        fields = ('name', 'age', 'creditcard', 'country', 'created', 'updated_at')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id','creditcard')

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ('phone','address')

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('currentmovie','watched','Recommended')

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id','genre')

class waystowatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = waystowatch
        fields = ('','')

class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ('','')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('','')
