from django.db import models


class TestSession(models.Model):
    test_sessionid = models.BigIntegerField(db_column='test_SessionID', primary_key=True)  # Field name made lowercase.
    test_type = models.BigIntegerField()
    test_idtest = models.BigIntegerField(db_column='Test_IDtest')  # Field name made lowercase.
    dataurl = models.CharField(db_column='DataURL', max_length=-1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Test_Session'
        unique_together = (('test_sessionid', 'test_type', 'test_idtest', 'dataurl'),)


class AllData(models.Model):
    exercise_id = models.BigIntegerField(db_column='Exercise_id', primary_key=True)  # Field name made lowercase.
    no_sessions_field = models.BigIntegerField(db_column='No.sessions ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day_field = models.CharField(db_column='Day ', max_length=-1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    week = models.BigIntegerField(db_column='Week', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    exercise = models.CharField(db_column='Exercise', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_data'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class clinicAnswer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey('clinicQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_answer'


class clinicData(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('clinicUser', models.DO_NOTHING)
    exercise = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'clinic_data'


class clinicExercise(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'clinic_exercise'


class clinicPlay(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clinic_play'


class clinicQuestion(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey('clinicQuiz', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_question'


class clinicQuiz(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('clinicUser', models.DO_NOTHING)
    subject = models.ForeignKey('clinicSubject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_quiz'


class clinicResearcher(models.Model):
    user = models.OneToOneField('clinicUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'clinic_researcher'


class clinicSalesrecord(models.Model):
    region = models.CharField(db_column='Region', max_length=100)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    totalsales = models.IntegerField(db_column='TotalSales')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinic_salesrecord'


class clinicStudent(models.Model):
    user = models.OneToOneField('clinicUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'clinic_student'

        """
class clinicStudentInterests(models.Model):
    student = models.ForeignKey(clinicStudent, models.DO_NOTHING)
    subject = models.ForeignKey('clinicSubject', models.DO_NOTHING)
    """
    class Meta:
        managed = False
        db_table = 'clinic_student_interests'
        unique_together = (('student', 'subject'),)


class clinicStudentanswer(models.Model):
    answer = models.ForeignKey(clinicAnswer, models.DO_NOTHING)
    student = models.ForeignKey(clinicStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_studentanswer'


class clinicSubject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'clinic_subject'


class clinicTakenexercise(models.Model):
    score = models.FloatField()
    date = models.DateTimeField()
    quiz = models.ForeignKey(clinicData, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_takenexercise'


class clinicTakenquiz(models.Model):
    score = models.FloatField()
    date = models.DateTimeField()
    quiz = models.ForeignKey(clinicQuiz, models.DO_NOTHING)
    student = models.ForeignKey(clinicStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_takenquiz'


class clinicUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    is_researcher = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'clinic_user'


class clinicUserGroups(models.Model):
    user = models.ForeignKey(clinicUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_user_groups'
        unique_together = (('user', 'group'),)


class clinicUserUserPermissions(models.Model):
    user = models.ForeignKey(clinicUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DashboardEx1(models.Model):
    exercise_category = models.CharField(max_length=20)
    time_of_day = models.CharField(max_length=50)
    minutes = models.CharField(max_length=50)
    intensity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'dashboard_ex1'


class DashboardPatient1(models.Model):
    day = models.CharField(db_column='Day', primary_key=True, max_length=20)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=20)  # Field name made lowercase.
    exercise_type = models.CharField(db_column='Exercise_type', max_length=20)  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    pulse = models.BigIntegerField(db_column='Pulse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_patient1'


class DashboardPatient3(models.Model):
    day = models.CharField(db_column='Day', primary_key=True, max_length=20)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=20)  # Field name made lowercase.
    exercise_type = models.CharField(db_column='Exercise_type', max_length=20)  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    pulse = models.BigIntegerField(db_column='Pulse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_patient3'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Patient1(models.Model):
    day = models.CharField(db_column='Day', primary_key=True, max_length=-1)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=-1)  # Field name made lowercase.
    exercise_type = models.CharField(db_column='Exercise_type', max_length=-1)  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    pulse = models.BigIntegerField(db_column='Pulse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient1'
        unique_together = (('day', 'month', 'exercise_type', 'time', 'pulse'),)


class Patient3(models.Model):
    day = models.CharField(db_column='Day', primary_key=True, max_length=-1)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=-1)  # Field name made lowercase.
    exercise_type = models.CharField(db_column='Exercise_type', max_length=-1)  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    pulse = models.BigIntegerField(db_column='Pulse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient3'
        unique_together = (('day', 'month', 'exercise_type', 'time', 'pulse'),)


class PatientData1(models.Model):
    patient1 = models.BigIntegerField(db_column='Patient1', primary_key=True)  # Field name made lowercase.
    patient2 = models.BigIntegerField(db_column='Patient2')  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_data1'
        unique_together = (('patient1', 'patient2', 'time'),)


class PatientData2(models.Model):
    patient1 = models.BigIntegerField(db_column='Patient1', primary_key=True)  # Field name made lowercase.
    patient2 = models.BigIntegerField(db_column='Patient2')  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    button = models.BigIntegerField(db_column='Button')  # Field name made lowercase.
    correct = models.BigIntegerField(db_column='Correct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_data2'
        unique_together = (('patient1', 'patient2', 'time', 'button', 'correct'),)


class PatientData3(models.Model):
    patient1 = models.BigIntegerField(db_column='Patient1', primary_key=True)  # Field name made lowercase.
    patient2 = models.BigIntegerField(db_column='Patient2')  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_data3'
        unique_together = (('patient1', 'patient2', 'time'),)


class PatientData4(models.Model):
    x = models.BigIntegerField(db_column='X', primary_key=True)  # Field name made lowercase.
    y = models.BigIntegerField(db_column='Y')  # Field name made lowercase.
    time = models.BigIntegerField(db_column='Time')  # Field name made lowercase.
    button = models.BigIntegerField(db_column='Button')  # Field name made lowercase.
    correct = models.BigIntegerField(db_column='Correct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_data4'
        unique_together = (('x', 'y', 'time', 'button', 'correct'),)


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
