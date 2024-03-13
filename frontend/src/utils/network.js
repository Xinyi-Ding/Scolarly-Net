const defaultOptions = {
  nodes: {
    borderWidth: 0,
    borderWidthSelected: 2,
    size: 8,
    shape: 'dot',
    font: {
      size: 10,
      vadjust: -5,
      face: 'Consolas',
    },
    color: '#154ec1'
  },
  edges: {
    font: {
      face: 'Consolas',
    },
    // smooth: {
    //   type: 'cubicBezier',
    //   forceDirection: 'horizontal',
    //   roundness: 0.4,
    // },
    smooth: {
      type: 'continuous',
    },
    color: {
      color: '#d1d5db',
      highlight: '#154ec1',
    },
  },
  physics: false, // disable graph physics
};

// add received options to default options
export const generateOptions = (customOptions) => {
  if (customOptions === undefined) return defaultOptions;
  return {
    ...defaultOptions,
    ...customOptions,
    nodes: {
      ...defaultOptions.nodes,
      ...customOptions.nodes,
      font: {
        ...defaultOptions.nodes.font,
        ...customOptions.nodes?.font,
      },
    },
    edges: {
      ...defaultOptions.edges,
      ...customOptions.edges,
      font: {
        ...defaultOptions.edges.font,
        ...customOptions.edges?.font,
      },
      color: {
        ...defaultOptions.edges.color,
        ...customOptions.edges?.color,
      },
    },
  };
};
