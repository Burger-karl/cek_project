from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Tag.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                suffix = f"-{counter}"
                slug = f"{base_slug[:50 - len(suffix)]}{suffix}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
    	if not self.slug:
        	base_slug = slugify(self.title)[:255]
        	slug = base_slug
        	counter = 1
        	while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            		suffix = f"-{counter}"
            		slug = f"{base_slug[:255 - len(suffix)]}{suffix}"
            		counter += 1
        	self.slug = slug
    	super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
