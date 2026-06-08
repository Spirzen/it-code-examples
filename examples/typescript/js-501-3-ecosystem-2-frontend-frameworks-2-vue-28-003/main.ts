
import { mount } from '@vue/test-utils'
import UserProfile from './UserProfile.vue'

test('отображает имя пользователя', () => {
  const wrapper = mount(UserProfile, {
    props: { name: 'Тимур' }
  })
  expect(wrapper.text()).toContain('Тимур')
})

test('вызывает событие при нажатии кнопки', async () => {
  const wrapper = mount(UserProfile, { props: { name: 'Тимур' } })
  await wrapper.get('button').trigger('click')
  expect(wrapper.emitted()).toHaveProperty('edit')
})
