from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.count if self.page else 0,
                "total_pages": self.page.paginator.num_pages if self.page else 0,
                "current_page": self.page.number if self.page else 1,
                "has_prev": bool(self.get_previous_link()),
                "has_next": bool(self.get_next_link()),
                "data": data,
            }
        )
