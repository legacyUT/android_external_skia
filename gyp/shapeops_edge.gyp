# GYP file to build unit tests.
{
  'includes': [
    'apptype_console.gypi',
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'edge',
      'type': 'executable',
      'include_dirs' : [
        '../src/core',
        '../src/gpu',
      ],
      'sources': [
        '../experimental/Intersection/ActiveEdge_Test.cpp',
        '../experimental/Intersection/ConvexHull.cpp',
        '../experimental/Intersection/ConvexHull_Test.cpp',
        '../experimental/Intersection/CubeRoot.cpp',
        '../experimental/Intersection/CubicBezierClip.cpp',
        '../experimental/Intersection/CubicBezierClip_Test.cpp',
        '../experimental/Intersection/CubicBounds.cpp',
        '../experimental/Intersection/CubicIntersection.cpp',
        '../experimental/Intersection/CubicIntersection_Test.cpp',
        '../experimental/Intersection/CubicIntersection_TestData.cpp',
        '../experimental/Intersection/CubicParameterization.cpp',
        '../experimental/Intersection/CubicParameterization_Test.cpp',
        '../experimental/Intersection/CubicParameterizationCode.cpp',
        '../experimental/Intersection/CubicReduceOrder.cpp',
        '../experimental/Intersection/CubicReduceOrder_Test.cpp',
        '../experimental/Intersection/CubicSubDivide.cpp',
        '../experimental/Intersection/CubicUtilities.cpp',
        '../experimental/Intersection/DataTypes.cpp',
        '../experimental/Intersection/EdgeMain.cpp',
        '../experimental/Intersection/EdgeWalker.cpp',
        '../experimental/Intersection/EdgeWalker_TestUtility.cpp',
        '../experimental/Intersection/EdgeWalkerPolygon4x4_Test.cpp',
        '../experimental/Intersection/EdgeWalkerPolygons_Mismatches.cpp',
        '../experimental/Intersection/EdgeWalkerPolygons_Test.cpp',
        '../experimental/Intersection/EdgeWalkerQuadralaterals_Test.cpp',
        '../experimental/Intersection/EdgeWalkerQuadratic4x4_Test.cpp',
        '../experimental/Intersection/EdgeWalkerQuadratics_Test.cpp',
        '../experimental/Intersection/EdgeWalkerRectangles_Test.cpp',
        '../experimental/Intersection/Extrema.cpp',
        '../experimental/Intersection/Inline_Tests.cpp',
        '../experimental/Intersection/Intersection_Tests.cpp',
        '../experimental/Intersection/IntersectionUtilities.cpp',
        '../experimental/Intersection/LineCubicIntersection.cpp',
        '../experimental/Intersection/LineCubicIntersection_Test.cpp',
        '../experimental/Intersection/LineIntersection.cpp',
        '../experimental/Intersection/LineIntersection_Test.cpp',
        '../experimental/Intersection/LineParameterization.cpp',
        '../experimental/Intersection/LineParameteters_Test.cpp',
        '../experimental/Intersection/LineQuadraticIntersection.cpp',
        '../experimental/Intersection/LineQuadraticIntersection_Test.cpp',
        '../experimental/Intersection/LineUtilities.cpp',
        '../experimental/Intersection/QuadraticBezierClip.cpp',
        '../experimental/Intersection/QuadraticBezierClip_Test.cpp',
        '../experimental/Intersection/QuadraticBounds.cpp',
        '../experimental/Intersection/QuadraticIntersection.cpp',
        '../experimental/Intersection/QuadraticIntersection_Test.cpp',
        '../experimental/Intersection/QuadraticIntersection_TestData.cpp',
        '../experimental/Intersection/QuadraticParameterization.cpp',
        '../experimental/Intersection/QuadraticParameterization_Test.cpp',
        '../experimental/Intersection/QuadraticReduceOrder.cpp',
        '../experimental/Intersection/QuadraticReduceOrder_Test.cpp',
        '../experimental/Intersection/QuadraticSubDivide.cpp',
        '../experimental/Intersection/QuadraticUtilities.cpp',
        '../experimental/Intersection/Simplify.cpp',
        '../experimental/Intersection/SimplifyAddIntersectingTs_Test.cpp',
        '../experimental/Intersection/SimplifyAngle_Test.cpp',
        '../experimental/Intersection/SimplifyFindNext_Test.cpp',
        '../experimental/Intersection/SimplifyFindTop_Test.cpp',
        '../experimental/Intersection/SimplifyNew_Test.cpp',
        '../experimental/Intersection/SimplifyRect4x4_Test.cpp',
        '../experimental/Intersection/TestUtilities.cpp',
        '../experimental/Intersection/CubicIntersection_TestData.h',
        '../experimental/Intersection/CubicUtilities.h',
        '../experimental/Intersection/CurveIntersection.h',
        '../experimental/Intersection/CurveUtilities.h',
        '../experimental/Intersection/DataTypes.h',
        '../experimental/Intersection/EdgeWalker_Test.h',
        '../experimental/Intersection/Extrema.h',
        '../experimental/Intersection/Intersection_Tests.h',
        '../experimental/Intersection/Intersections.h',
        '../experimental/Intersection/IntersectionUtilities.h',
        '../experimental/Intersection/LineIntersection.h',
        '../experimental/Intersection/LineParameters.h',
        '../experimental/Intersection/LineUtilities.h',
        '../experimental/Intersection/Parameterization_Test.h',
        '../experimental/Intersection/QuadraticIntersection_TestData.h',
        '../experimental/Intersection/QuadraticUtilities.h',
        '../experimental/Intersection/ShapeOps.h',
        '../experimental/Intersection/Simplify.h',
        '../experimental/Intersection/TestUtilities.h',
        '../experimental/Intersection/TSearch.h',
        '../experimental/Intersection/thingsToDo.txt',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'experimental.gyp:experimental',
        'gpu.gyp:gr',
        'gpu.gyp:skgr',
        'images.gyp:images',
        'ports.gyp:ports',
        'pdf.gyp:pdf',
        'utils.gyp:utils',
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
