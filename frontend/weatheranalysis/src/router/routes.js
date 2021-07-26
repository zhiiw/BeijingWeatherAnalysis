
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/index', component: () => import('pages/Index.vue')},
      { path: '/', component: () => import('pages/login.vue') },
      { path: '/about', component: () => import('pages/About.vue')},
      { path: '/login', component: () => import('pages/login.vue')},
      { path: '/reg', component: () => import('pages/reg.vue')},
      { path: '/temperature', component: () => import('pages/calendar.vue')},
      { path: '/wind', component: () => import('pages/test.vue')},



    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
