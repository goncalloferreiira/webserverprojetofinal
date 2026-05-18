from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Comentario

def index(request):
    filmes = Filme.objects.all()
    return render(request, 'index.html', {'filmes': filmes})

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    
    if request.method == 'POST':
        nome_autor = request.POST.get('autor')
        texto_comentario = request.POST.get('texto')
        nota_comentario = request.POST.get('nota')
        
        if nome_autor and texto_comentario and nota_comentario:
            Comentario.objects.create(
                filme=filme, 
                autor=nome_autor, 
                texto=texto_comentario,
                nota=nota_comentario
            )
            
        return redirect('detalhe_filme', filme_id=filme.id)
        
    return render(request, 'detalhe.html', {'filme': filme})

def apagar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    filme_id = comentario.filme.id
    
    comentario.delete()
    
    return redirect('detalhe_filme', filme_id=filme_id)