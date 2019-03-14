from django.db import models

#imagekit
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class Posting(models.Model) :
    content = models.TextField(default='')
    icon = models.CharField(max_length=20, default='')

    # save as origin
    # image = models.ImageField(blank=True, upload_to='postings/%y/%m/%d')
    image = ProcessedImageField(
        blank=True,
        upload_to='postings/resize/%y/%m/%d',
        processors=[ResizeToFit(width=960,upscale=False)],
        format='JPEG'
    )

    # 썸네일 이미지
    # 사용자로부터 이미지를 받아오는 것이 아니므로 upload_to옵션을 사용하지 않음
    # source의 값에는 이미지를 가지고 있는 칼럼이름!
    image_thumbnail =ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=320,upscale=False)],
        format='JPEG',
        options={'quality':60}
    )
    # auto_now_add : 생성되고 나서 한번만 기록, 
    # auto_now : 생성 이후로도 수정될때도 기록
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}:{self.content[:20]}'

    # DB 저장시, 로그찍기
    def save(self, *args, **kwargs):
        # 일단 원래하던 save() 수행
        super().save(*args,**kwargs)
        # 로그 찍기
        print()
        print(f'=== Saved Posting with id: {self.id} ===')
        print(f'    content: {self.content}')
        if self.image :
            print(f'    image: {self.image.width}.px * {self.image.height}.px : {self.image.size/1024} kb')
        print(f'=================================')


class Comment(models.Model) :
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, default="")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posting.content[:20]}:{self.content[:20]}'

