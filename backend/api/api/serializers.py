from api.models import Product

from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(max_length=255)
    
    #ajout de fonction depuis le models Product
    price_in_euros = serializers.SerializerMethodField()
    description_in_euros = serializers.SerializerMethodField()
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    # cela fat appel a tout les champs du models
    class Meta:
        model = Product
        fields = '__all__'
        #read_only_fields = ['created_at', 'updated_at']
        
    def get_price_in_euros(self, obj):
        return obj.get_price_in_euros()
    
    def get_description_in_euros(self, obj):
        return obj.get_description()
        
    #Validation de certain condition sur le name avec le champs name declarer en haut   
    def validate_name(self, value):
        if value in ['ESCANOR', 'LION']:
            raise serializers.ValidationError('Your are not allowed to use this name')
        return value
    
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