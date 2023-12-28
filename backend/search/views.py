# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import sys
sys.path.append("./engine")
from engine.searching.search import get_results

class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        search_query = request.query_params.get('q', '')  # Assuming the search query is passed as a URL parameter 'q'
        results = get_results(search_query)
        return Response(results[:30])
