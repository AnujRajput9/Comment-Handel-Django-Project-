# Comment-Handel-Django-Project-
🔹 1. Create (Insert Data)

Creating a comment using a ModelForm:

def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("comment_list")
    else:
        form = CommentForm()
    return render(request, "comment_form.html", {"form": form})


✔ Data is validated
✔ Stored in the database using .save()

🔹 2. Read (Fetch Data)

Fetching all comments from the database:

def comment_list(request):
    comments = Comment.objects.all().order_by("-created_at")
    return render(request, "comment_list.html", {"comments": comments})


✔ Uses Django ORM
✔ Data passed to template
✔ Rendered dynamically using template loops

🔹 3. Update (Edit Data)

Updating an existing comment:

def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    form = CommentForm(request.POST or None, request.FILES or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect("comment_list")
    return render(request, "comment_form.html", {"form": form})


✔ Uses instance parameter
✔ Only owner can edit
✔ Updates existing record, not creates new

🔹 4. Delete (Remove Data)

Deleting a comment:

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    comment.delete()
    return redirect("comment_list")


✔ Secure deletion
✔ Ownership check
✔ Removes record permanently

🗄️ Database Model Example
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="comments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


✔ Django ORM handles SQL automatically
✔ No manual SQL queries required

🧩 Template Inheritance

All pages extend a single base layout:

{% extends "layout.html" %}
{% block content %}
{% endblock %}


✔ Consistent design
✔ Easy maintenance
✔ Professional structure

⚙️ How to Run This Project
1️⃣ Clone Repository
git clone https://github.com/your-username/comment-management-django.git
cd comment-management-django

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run Server
python manage.py runserver

6️⃣ Open Browser
http://127.0.0.1:8000/

🔐 Security Measures

CSRF Protection enabled

Authentication required for CRUD

Ownership checks before update/delete

Secure media handling
