# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import sys
import time
sys.path.append("./engine")
from engine.searching.search import get_results

class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        search_query = request.query_params.get('q', '')  # Assuming the search query is passed as a URL parameter 'q'
        start_time = time.time()
        results = get_results(search_query)
        end_time = time.time()
        total_time = (end_time-start_time)
        total_results = len(results)

        res = {
            "time":total_time,
            "count":total_results,
            "result":results
        }

        return Response(res)
