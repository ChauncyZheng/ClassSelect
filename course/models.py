from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name=r'教师姓名', unique=True)
    phone_number = models.CharField(max_length=11, verbose_name=r'电话号码')
    password = models.CharField(max_length=256, verbose_name=r'密码', default=r'123456')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'教师'
        verbose_name_plural = verbose_name


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name=r'学生姓名')
    class_id = models.CharField(
        choices=(('dq1', '电气1班'), ('dq2', '电气2班'), ('dx1', '电信1班'), ('dx2', '电信2班')),
        verbose_name=r'班级',
        max_length=3,
        default='dq1',
    )
    phone_number = models.CharField(max_length=11, verbose_name=r'手机号码')
    email = models.EmailField(max_length=20, verbose_name=r'邮箱', unique=True)
    school_id = models.CharField(max_length=10, verbose_name=r'学号')
    password = models.CharField(max_length=256, verbose_name=r'密码')
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = r'学生'
        verbose_name_plural = verbose_name


class Course(models.Model):
    teacher = models.ForeignKey('Teacher', verbose_name=r'教师')
    name = models.CharField(max_length=100, verbose_name=r'课程名')
    describe = models.TextField(max_length=200, verbose_name=r'课程描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'课程'
        verbose_name_plural = verbose_name


class Question(models.Model):
    course = models.ForeignKey('Course', verbose_name=r'课程名')
    name = models.CharField(max_length=100, verbose_name=r'问题标题')
    content = models.TextField(max_length=200, verbose_name=r'问题内容')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = r'课后问题'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(r'Course', verbose_name=r'课程名')
    name = models.CharField(max_length=100, verbose_name=r'资源文件名')
    file = models.FileField(upload_to='uploads/', max_length=500, verbose_name='课程资源文件')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name=r'上传时间')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = r'课程资源'
        verbose_name_plural = verbose_name


class CourseSelect(models.Model):
    student = models.ForeignKey('Student', verbose_name=r'学生')
    course = models.ForeignKey('Course', verbose_name=r'课程')

    def __str__(self):
        name = '%s\t%s' % (self.student.name, self.course.name)
        return name

    class Meta:
        unique_together = ('student', 'course')
        verbose_name = r'选课情况'
        verbose_name_plural = verbose_name


class Answer(models.Model):
    question = models.ForeignKey('Question', verbose_name=r'问题')
    student = models.ForeignKey('Student', verbose_name=r'作答学生')
    reply = models.TextField(max_length=200, verbose_name=r'作答内容')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = '%s\t%s' % (self.question.name, self.student.name)
        return name

    class Meta:
        unique_together = ('question', 'student')
        ordering = ['-c_time']
        verbose_name = r'学生作答情况'
        verbose_name_plural = verbose_name


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('Student')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
