from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings as _settings
from command.models import * 
import json
import subprocess


def update(request, *args, **kwargs):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        for item in _settings.RESPOSITORY_KEY_NAME:
            keys = _settings.item.split('.')
            name = body
            project = False
            try:
                for key in keys:
                    name = name[key]
                project = Project.objects.get(git_name=name)
                commands = Command.objects.filter(project=project)
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
                pass
    except Exception as error:
        pass
    return HttpResponse('ok', content_type='application/json; charset=utf-8')