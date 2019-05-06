from django.conf import settings as _settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from command.models import * 
import json
import subprocess


@csrf_exempt
def update(request, *args, **kwargs):
    lista = []
    dicc = {}
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for item in _settings.RESPOSITORY_KEY_NAME:
            keys = item.split('.')
            name = body
            project = False
            try:
                for key in keys:
                    name = name[key]
                project = Project.objects.get(git_name=name, is_active=True)
                commands = Command.objects.filter(project=project).order_by('position')
                update = Update(
                    project=project,
                    request=body_unicode,
                )
                update.save()
                for command in commands:
                    respuesta = ''
                    try:
                        respuesta = subprocess.check_output(
                            command.command,
                            stderr=subprocess.STDOUT,
                            shell=True
                        )
                        try:
                            respuesta = respuesta.decode("utf-8")
                        except Exception as errorDecode:
                            pass
                    except Exception as errorXjecute:
                        error = True 
                        respuesta = errorXjecute.stdout
                        try:
                            respuesta = respuesta.decode()
                        except Exception as errorDecodeXjecute:
                            respuesta = errorXjecute.stdout
                            pass
                    Update_log = UpdateLog(
                        update=update,
                        Command=command.command,
                        log=respuesta,
                    )
                    Update_log.save()
            except Exception as identifier:
                lista.append({"error":identifier})
    except Exception as error:
        lista.append({"error":error})
    return HttpResponse('ok', content_type='application/json; charset=utf-8')