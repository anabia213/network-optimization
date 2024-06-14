import pandas as pd
from django.shortcuts import render
from .models import NetworkData

def analyze_network_data():
    # Importe os dados usando Pandas
    df = pd.read_csv('network_data.csv')

    # Analise os dados conforme necessário
    # Exemplo: Identifique áreas com problemas de cobertura ou capacidade
    problematic_areas = df[df['signal_strength'] < 80]
    return problematic_areas

def network_data(request):
    # Recupere os dados do banco de dados
    data = NetworkData.objects.all()
    return render(request, 'network_data.html', {'data': data})
