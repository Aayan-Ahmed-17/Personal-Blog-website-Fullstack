BLOG_GRID_CONTAINER = "div.grid.w-full.grid-cols-1.gap-4.p-2"  # container for all blogs
BLOG_CONTAINER = "div.p-6.bg-white.rounded-xl"  # container for each blog post | through BLOG_GRID_CONTAINER | apply for loop

BLOG_LINK = "div a.group"  # link of each blog post | through BLOG_CONTAINER
IMG_TAG = "div a div img.w-full.h-auto.transition-all.transition.duration-200.ease-in-out.lightense-target"  # image tag of each blog post | through BLOG_CONTAINER
TITLE_TAG = "div a h3"  # title of each blog post | through BLOG_CONTAINER
DATE_TAG = "div div div span.text-gray-500"  # date tag of each blog post | through BLOG_CONTAINER | apply for loop to get 2 spans, then select the second one for the latest date
DESCRIPTION_TAG = "div div p.mt-6.leading-normal.text-gray-600.line-clamp-3"  # description of each blog post | through BLOG_CONTAINER
