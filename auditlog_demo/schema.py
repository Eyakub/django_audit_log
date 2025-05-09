import graphene
from graphene_django import DjangoObjectType
from core.models import Task
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'created_by', 
                 'created_at', 'updated_at')


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType, id=graphene.ID(required=True))

    def resolve_tasks(self, info):
        print("resolve_tasks==========", info.context)
        if not info.context.user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(created_by=info.context.user)

    def resolve_task(self, info, id):
        if not info.context.user.is_authenticated:
            return None
        return Task.objects.filter(created_by=info.context.user, id=id).first()


class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)

    def mutate(self, info, title, description="", completed=False):
        if not info.context.user.is_authenticated:
            raise Exception("You must be logged in to create a task")

        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            created_by=info.context.user
        )
        return CreateTask(task=task)


class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)

    def mutate(self, info, id, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception("You must be logged in to update a task")

        task = Task.objects.filter(created_by=info.context.user, id=id).first()
        if not task:
            raise Exception("Task not found")

        for key, value in kwargs.items():
            if value is not None:
                setattr(task, key, value)

        task.save()
        return UpdateTask(task=task)


class DeleteTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        if not info.context.user.is_authenticated:
            raise Exception("You must be logged in to delete a task")

        task = Task.objects.filter(created_by=info.context.user, id=id).first()
        if not task:
            raise Exception("Task not found")

        task.delete()
        return DeleteTask(success=True)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
