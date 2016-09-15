from django.core.urlresolvers import reverse
from django.views.generic import View

from problems.forms.validator import ValidatorAddForm
from problems.models import Validator
from problems.views.decorators import authenticate_problem_access
from problems.views.generics import ProblemObjectDeleteView, ProblemObjectAddView
from problems.views.utils import render_for_problem


class ValidatorsListView(View):
    @authenticate_problem_access("read_validators")
    def get(self, request, problem, revision):
        validators = revision.validator_set.all()

        return render_for_problem(request, problem, revision, "problems/validator_list.html", context={
            "validators": validators
        })


class ValidatorEditView(View):
    pass


class ValidatorAddView(ProblemObjectAddView):
    template_name = "problems/add_validator.html"
    model_form = ValidatorAddForm
    permissions_required = ["add_validator"]

    def get_success_url(self, problem, revision, obj):
        return reverse("problems:add_validator", kwargs={
            "problem_id": problem.id,
            "revision_id": revision.id,
        })


ValidatorDeleteView = ProblemObjectDeleteView.as_view(
    object_type=Validator,
    permissions_required="delete_validator",
    redirect_to="problems:validators"
)