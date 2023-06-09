# Generated by Django 4.2 on 2023-05-21 16:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ministry', models.CharField(max_length=500)),
                ('contractor', models.CharField(max_length=500)),
                ('local_gov', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('contract_sum', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'in progress'), ('DONE', 'done')], max_length=20)),
                ('priority', models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], max_length=20)),
                ('user_assigned', models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_disbursed', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_spent', models.DecimalField(decimal_places=2, max_digits=20)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='pd_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=500)),
                ('head', models.CharField(max_length=500)),
                ('members', models.CharField(max_length=500)),
                ('projects', models.ManyToManyField(to='pd_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('note', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'in progress'), ('DONE', 'done')], max_length=20)),
                ('priority', models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], max_length=20)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='pd_app.project')),
                ('users_assigned', models.ManyToManyField(blank=True, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=500)),
                ('uploaded_at', models.DateField()),
                ('file_url', models.CharField(max_length=1000)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pd', to='pd_app.project')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pd', to='pd_app.task')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('milestone_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('progress', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('tag', models.CharField(choices=[('ON_SCHEDULE', 'on schedule'), ('BEHIND_SCHEDULE', 'behind schedule')], max_length=20)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestone', to='pd_app.project')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestone', to='pd_app.task')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=2500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Action',
            fields=[
                ('issue_action_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2000)),
                ('committed_by', models.CharField(max_length=500)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='pd_app.project')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='pd_app.task')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pd_app.project'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
