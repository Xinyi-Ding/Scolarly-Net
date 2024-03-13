import { mount } from '@vue/test-utils'
import { describe, expect, it, beforeEach } from "vitest";
import SearchResult from "@/components/SearchResult.vue";

describe('SearchResult', () => {
  let wrapper;

  beforeEach(() => {
    const searchResults = [
      { id: 1, title: 'First Result', subtitle: 'First subtitle' },
      { id: 2, title: 'Second Result', subtitle: 'Second subtitle' }
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
    const searchResults = wrapper.findAll('.p-2.cursor-pointer.hover:bg-gray-100');
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
