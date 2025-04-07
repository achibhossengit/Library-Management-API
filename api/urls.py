from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from book.views import BookViewSet, CategoryViewSet
from author.views import AuthorViewSet, AuthorsBookViewSet
from users.views import MemberViewSet
from borrow_book.views import BorrowViewSet, MemberBorrowViewSet

routers = DefaultRouter()
routers.register('books', BookViewSet)
routers.register('categories', CategoryViewSet)
routers.register('authors', AuthorViewSet)
routers.register('members', MemberViewSet)
routers.register('borrow-list', BorrowViewSet)

author_router = NestedDefaultRouter(routers,'authors', lookup='author')
author_router.register('books', AuthorsBookViewSet, basename='author-books')

member_router = NestedDefaultRouter(routers, 'members',lookup='member')
member_router.register('borrow-list', MemberBorrowViewSet, basename='memeber-borrow-books')

# borrow_router = NestedDefaultRouter(routers, 'borrow-list', lookup='borrow_record')
# borrow_router.register('mem')

urlpatterns = [
    path('', include(routers.urls)),
    path('', include(author_router.urls)),
    path('', include(member_router.urls)),
    # path('authors/<author_pk>/books', AuthorsBookViewSet.as_view({'get':'list'})),
    # path('authors/<author_pk>/books/<pk>/', AuthorsBookViewSet.as_view({'get':'retrieve'})),
]

