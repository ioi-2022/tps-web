from django.core.urlresolvers import reverse
from django.http import Http404

from problems.forms.statement import StatementForm
from problems.models import StatementAttachment, Statement
from problems.views.utils import get_git_object_or_404
from problems.views.generics import ProblemObjectEditView, RevisionObjectView, ProblemObjectDownloadView


__all__ = ["EditStatement", "DownloadStatementAttachment"]


class EditStatement(ProblemObjectEditView):
    template_name = "problems/statement.html"
    model_form = StatementForm
    permissions_required = "observe"
    http_method_names_requiring_edit_access = RevisionObjectView.http_method_names_requiring_edit_access
    UPDATED_TO_GIT = True

    def get_success_url(self, request, problem_code, revision_slug, obj):
        return reverse("problems:statement", kwargs={
            "problem_code": problem_code,
            "revision_slug": revision_slug
        })

    def get_instance(self, request, *args, **kwargs):
        return Statement.objects.get()


class DownloadStatementAttachment(ProblemObjectDownloadView):
    def get_file(self, request, *args, **kwargs):
        attachment_id = kwargs.get('attachment_id')
        return get_git_object_or_404(StatementAttachment, pk=attachment_id, problem=self.revision).file

    def get_name(self, request, *args, **kwargs):
        attachment_id = kwargs.get('attachment_id')
        return get_git_object_or_404(StatementAttachment, pk=attachment_id, problem=self.revision).name