from django.shortcuts import render
from django.http import HttpResponse

FAKE_DB_PROJECTS = [
  f'https://picsum.photos/id/{id}/100/80' for id in range(21,29)
]

FAKE_DB_CAROUSEL = [
  f'https://picsum.photos/id/{id}/1200/400' for id in range(48, 52)
]
# Create your views here.
def home(request):
  hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec malesuada turpis. Suspendisse a rhoncus nisl, sed dignissim quam. Cras in erat condimentum, viverra leo et, rhoncus odio. Fusce sed purus libero. Suspendisse ut aliquet lectus. Mauris sit amet lectus semper, fringilla ex tempus, dictum tellus. Proin mi ante'
  context = dict(
    hero_content = hero_content,
    FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
    FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
  )
  return render(request, "pages/index.html", context)

def about_us(request):
  page_title = 'Hakkimizda'
  hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec malesuada turpis. Suspendisse a rhoncus nisl, sed dignissim quam. Cras in erat condimentum, viverra leo et, rhoncus odio. Fusce sed purus libero. Suspendisse ut aliquet lectus. Mauris sit amet lectus semper, fringilla ex tempus, dictum tellus. Proin mi ante'
  context = dict(
    page_title = page_title,
    hero_content = hero_content,
    FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
  )
  return render(request, "pages/about_us.html", context)

def contact_us(request):
  page_title = 'Iletisim'
  hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec malesuada turpis. Suspendisse a rhoncus nisl, sed dignissim quam. Cras in erat condimentum, viverra leo et, rhoncus odio. Fusce sed purus libero. Suspendisse ut aliquet lectus. Mauris sit amet lectus semper, fringilla ex tempus, dictum tellus. Proin mi ante"
  context = dict(
    page_title = page_title,
    hero_content = hero_content,
    FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
  )
  return render(request, "pages/contact.html", context)

def vision_us(request):
  page_title = 'Vizyonumuz'
  hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec malesuada turpis. Suspendisse a rhoncus nisl, sed dignissim quam. Cras in erat condimentum, viverra leo et, rhoncus odio. Fusce sed purus libero. Suspendisse ut aliquet lectus. Mauris sit amet lectus semper, fringilla ex tempus, dictum tellus. Proin mi ante'
  context = dict(
    page_title = page_title,
    hero_content = hero_content,
    FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
  )
  return render(request, "pages/vision_us.html", context)