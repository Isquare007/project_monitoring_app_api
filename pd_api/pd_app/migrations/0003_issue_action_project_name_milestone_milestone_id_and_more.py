# Generated by Django 4.2 on 2023-04-21 01:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pd_app', '0002_task_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_action',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issueaction', to='pd_app.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milestone',
            name='milestone_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='milestone',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to='pd_app.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project_document',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_doc', to='pd_app.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='pd_app.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='pd_app.project'),
            preserve_default=False,
        ),
    ]