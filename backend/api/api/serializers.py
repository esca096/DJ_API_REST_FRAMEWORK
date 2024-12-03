from api.models import Product

from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    # cela fat appel a tout les champs du models
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    # c'est une surchage de methode pour ajouter la champs email   
    def create(self, validated_data):
        email = validated_data.pop('email')
        print('email:', email )
        return super().create(validated_data)

# elle fait l'appel a un certain normbre de champs specifique du models'
class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    
    # cette fonction permet de pouvoir instancier cette class grace a une surcharge de methode
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)