from django.shortcuts import render
from django.http import JsonResponse
from processV.models import ProcessData
from django.core.paginator import Paginator

def chart_view(request):
    return render(request, 'chart/chart.html')

def process_data_chart(request):
    try:
        # Define the number of items per page
        items_per_page = 100

        # Get the page number from the request
        page_number = request.GET.get('page', 1)

        # Fetch only the required fields
        data = ProcessData.objects.values(
            'timestamp', 'p_reactor', 't_reactor', 't_hotoil_in_target',
            't_hotoil_in', 't_hotoil_out', 't_reactor_target', 'n_stirrer_target',
            'n_stirrer', 'n_homog_target', 'n_homog', 'i_homog', 'i_stirrer',
            'v_exh', 'pos_mh'
        ).order_by('timestamp')

        # Paginate the data
        paginator = Paginator(data, items_per_page)
        page_obj = paginator.get_page(page_number)

        # Serialize the paginated data
        chart_data = {
            'timestamps': [entry['timestamp'].strftime("%Y-%m-%d %H:%M:%S") for entry in page_obj],
            'p_reactor': [entry['p_reactor'] for entry in page_obj],
            't_reactor': [entry['t_reactor'] for entry in page_obj],
            't_hotoil_in_target': [entry['t_hotoil_in_target'] for entry in page_obj],
            't_hotoil_in': [entry['t_hotoil_in'] for entry in page_obj],
            't_hotoil_out': [entry['t_hotoil_out'] for entry in page_obj],
            't_reactor_target': [entry['t_reactor_target'] for entry in page_obj],
            'n_stirrer_target': [entry['n_stirrer_target'] for entry in page_obj],
            'n_stirrer': [entry['n_stirrer'] for entry in page_obj],
            'n_homog_target': [entry['n_homog_target'] for entry in page_obj],
            'n_homog': [entry['n_homog'] for entry in page_obj],
            'i_homog': [entry['i_homog'] for entry in page_obj],
            'i_stirrer': [entry['i_stirrer'] for entry in page_obj],
            'v_exh': [entry['v_exh'] for entry in page_obj],
            'pos_mh': [entry['pos_mh'] for entry in page_obj],
            'page': page_obj.number,
            'num_pages': paginator.num_pages
        }
        return JsonResponse(chart_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
