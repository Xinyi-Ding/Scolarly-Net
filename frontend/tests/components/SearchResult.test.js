import { mount } from '@vue/test-utils'
import { describe, expect, it, beforeEach } from "vitest";
import SearchResult from "@/components/SearchResult.vue";

describe('SearchResult', () => {
  let wrapper;

  beforeEach(() => {
    const searchResults = [
      { articleId: 1, title: 'First Result', authors: [{authorId: 1, name: 'test'}] },
      { articleId: 2, title: 'Second Result', authors: [{authorId: 1, name: 'test'}] }
    ];

    wrapper = mount(SearchResult, {
      props: {
        modelValue: true,
        search: 'test',
        searchResults: searchResults
      }
    });
  });

  it('does not render search results when there are none', () => {
    const wrapper = mount(SearchResult, {
      props: {
        modelValue: true,
        search: 'test',
        searchResults: []
      }
    });
    const searchResults = wrapper.findAll('.va-list-item');
    expect(searchResults.length).toBe(0);
  });

  it('emits "update:modelValue" when the modal is closed', async () => {
    await wrapper.vm.handleClose();
    expect(wrapper.emitted('update:modelValue')).toBeTruthy();
    expect(wrapper.emitted('update:modelValue')[0]).toEqual([false]);
  });

  it('does not emit "select" when no search result is clicked', async () => {
    expect(wrapper.emitted('select')).toBeFalsy();
  });

});
