export const routesConfig = [
  {
    path: '/topic',
    name: 'topic',
    title: 'Topic',
    icon: 'topic',
    redirect: '/topic/same-topic',
    children: [
      {
        path: '/topic/same-topic',
        name: 'same-topic',
        title: 'Same Topic List',
        icon: 'list',
        component: () => import('../views/topic/SameTopicList.vue')
      },
      {
        path: '/topic/connections',
        name: 'connections',
        title: 'Topic Connections',
        icon: 'hub',
        component: () => import('../views/topic/TopicConnections.vue')
      },
    ]
  },
  {
    path: '/author',
    name: 'author',
    title: 'Author',
    icon: 'person',
    redirect: '/author/co-author',
    children: [
      {
        path: '/author/co-author',
        name: 'co-author',
        title: 'Co-Author',
        icon: 'groups',
        component: () => import('../views/author/CoAuthor.vue')
      },
    ]
  },
  {
    path: '/reference',
    name: 'reference',
    title: 'Reference',
    icon: 'link',
    redirect: '/reference/cited',
    children: [
      {
        path: '/reference/cited',
        name: 'cited',
        title: 'Cited Tree',
        icon: 'vertical_align_top',
        component: () => import('../views/reference/CitedTree.vue')
      },
      {
        path: '/reference/cited-by',
        name: 'cited-by',
        title: 'Cited By Tree',
        icon: 'vertical_align_bottom',
        component: () => import('../views/reference/CitedByTree.vue')
      },
    ]
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    title: 'Dashboard',
    icon: 'dashboard',
    component: () => import('../views/Dashboard.vue')
  }
];
