from  rest_framework import  serializers
from  .models import BLOG,Categories,Contact


class categorieSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields =['id','name','blog']
    def validate(self, attrs):
        # print(self.context['request'].user)
        if len(attrs) >3:
            raise serializers.ValidationError({'title':'lenth 3'})

        print(attrs)
        return attrs


class blogSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=False,read_only=False)
    class Meta:
        model = BLOG
        fields =['id','title','Image','Active','Featured','Description','categories',]



class blogSerializerCreate(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     blog = BLOG()
    #     blog.title = request.user
    #     blog.categories = validated_data['categories']
    #     blog.Active = validated_data['Active']
    #     blog.Featured = validated_data['Featured']
    #     blog.Description = validated_data['Description']
    #     blog.Image = validated_data['Image']
    #     blog.save()
    #     return blog
    class Meta:
        model = BLOG
        fields =['id','title','Image','Active','Featured','Description','categories',]

    def validate(self, attrs):
        k = attrs['Description']
        if len(k)<10:
            raise serializers.ValidationError({'Description':'mini 10 world'})
        return attrs


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ="__all__"
