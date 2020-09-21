from django.shortcuts import render, get_object_or_404, redirect, reverse



class DetailMixin:
    """ Mixin, для объединения общей логики, представления поста и тега """
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render (request, self.template, {self.model.__name__.lower():obj, 'detail_obj':True, 'obj':obj})


class CreateMixin:
    """ Mixin, для объединения общей логики, представления формы создания постов и тегов """
    form_model = None
    template = None
    def get(self, request):
        form = self.form_model()
        return render(request, self.template, {'form':form})
    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, self.template, {'form': bound_form})


class UpdateMixin:
    """ Mixin, для объединения общей логики, представления формы обновления постов и тегов """
    model = None
    form_model = None
    template = None
    def get(self, request, slug):
        obj_model = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj_model)
        return render(request, self.template, {'form': form, self.model.__name__.lower(): obj_model})
    def post(self, request, slug):
        obj_model = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj_model)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return (request, self.template, {'form': bound_form, self.model.__name__.lower(): obj_model})


class DeleteMixin:
    """ Mixin, для объединения общей логики, представления формы удаления постов и тегов """
    model = None
    template = None
    good_luck_address = None
    def get(self, request, slug):
        obj_model = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower():obj_model})
    def post(self, request, slug):
        obj_model = self.model.objects.get(slug__iexact=slug)
        obj_model.delete()
        return redirect(reverse(self.good_luck_address))
