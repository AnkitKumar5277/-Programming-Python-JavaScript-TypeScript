import { test, expect } from '@playwright/test';
test('Dropdown Example', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/dropdown');
  await page.selectOption('#dropdown', {label: 'Option 1' });
  console.log('Selected Option 1');
  await page.selectOption('#dropdown', {value: '2'});
  console.log('Selected Option 2');
  await page.selectOption('#dropdown', {index: 1});
  console.log('Selected by index');
  await expect(page.locator('#dropdown')).toHaveValue('1');
  console.log('Dropdown test completed successfully');
});
