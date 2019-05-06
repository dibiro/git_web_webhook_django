from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=500)
    git_name = models.CharField(max_length=500, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'project'
        verbose_name_plural = "projects"
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Command(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='command_projects')
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)
    command = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField()
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'command'
        verbose_name_plural = "commands"

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Update(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_updates')
    request = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'update'
        verbose_name_plural = "updates"

    def __unicode__(self):
        return '%s' % (self.project)

    def __str__(self):
        return '%s' % (self.project)


class UpdateLog(models.Model):
    update = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='items')
    Command = models.TextField()
    log = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'update_item'
        verbose_name_plural = "update_items"

    def __unicode__(self):
        return '%s' % (self.project)

    def __str__(self):
        return '%s' % (self.project)