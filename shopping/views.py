from rest_framework import viewsets, permissions
from .models import ShoppingList
from .serializers import ShoppingListSerializer

class ShoppingListViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
