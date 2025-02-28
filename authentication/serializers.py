from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        """إنشاء مستخدم جديد مع تشفير كلمة المرور"""
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])  # تشفير كلمة المرور
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get("username")  # هذا الحقل يستقبل البريد أو اسم المستخدم
        password = attrs.get("password")

        # التحقق مما إذا كان الإدخال بريدًا إلكترونيًا أو اسم مستخدم
        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                raise serializers.ValidationError({"error": "No active account found with the given credentials"})

        # التحقق من صحة كلمة المرور
        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Incorrect credentials"})

        # تحديث `username` ليتم تمريره للنظام الأساسي لـ JWT
        attrs["username"] = user.username
        return super().validate(attrs)