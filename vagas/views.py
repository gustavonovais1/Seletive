from django.shortcuts import render
from django.http import HttpResponse, Http404
from empresa.models import Vagas
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tarefa, Emails
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        vagas = Vagas( 
                    titulo=titulo,
                    email=email,
                    nivel_experiencia=experiencia,
                    data_final=data_final,
                    empresa_id=empresa,
                    status=status,
        )

        vagas.save()

        vagas.tecnologias_estudar.add(*tecnologias_nao_domina)
        vagas.tecnologias_dominadas.add(*tecnologias_domina)

        vagas.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        
        return redirect(f'/home/empresa/{empresa}')

    elif request.method == "GET":
        raise Http404()

def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizadas=False)
    emails = Emails.objects.filter(vaga=vaga)
    return render(request, 'vaga.html', {'vaga': vaga, 'tarefas': tarefas, 'emails': emails})

def nova_tarefa(request, id_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')

    try:
        tarefa = Tarefa(vaga_id=id_vaga,
                        titulo=titulo,
                        prioridade=prioridade,
                        data=data
                        )

        tarefa.save()
        messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
        return redirect(f'/vagas/vaga/{id_vaga}')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect(f'/vagas/vaga/{id_vaga}')

def realizar_tarefa(request, id ):
    tarefa_list = Tarefa.objects.filter(id=id).filter(realizadas=False)

    if not tarefa_list.exists():
        messages.add_message(request, constants.ERROR, 'Realize apenas uma tarefa por vez')
        return redirect('/home/empresas')

    tarefa = tarefa_list.first()
    tarefa.realizadas = True
    tarefa.save()       
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{tarefa.vaga.id}')

def envia_email(request, id_vaga):
    vaga = Vagas.objects.get(id=id_vaga)
    assunto = request.POST.get('assunto')
    corpo = request.POST.get('corpo')

    html_content = render_to_string('emails/template_email.html', {'corpo': corpo})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, [vaga.email,] )

    email.attach_alternative(html_content, 'text/html')
    if email.send(): 
        meil = Emails(
            vaga=vaga,
            assunto=assunto,
            corpo=corpo,
            enviado=True
        )
        meil.save()
        messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso!')
        return redirect(f'/vagas/vaga/{id_vaga}')
    else:
        meil = Emails(
            vaga=vaga,
            assunto=assunto,
            corpo=corpo,
            enviado=False
        )
        meil.save()
        messages.add_message(request, constants.ERROR, 'Falha no envio do email, tente novamente mais tarde.')
        return redirect(f'/vagas/vaga/{id_vaga}')