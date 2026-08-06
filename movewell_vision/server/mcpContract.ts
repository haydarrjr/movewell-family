/**
 * Model Context Protocol (MCP) Public Contract for Movewell Vision.
 */

export interface MCPToolDescriptor {
  name: string;
  description: string;
  inputSchema: object;
}

export const MOVEWELL_VISION_MCP_CONTRACT = {
  contractName: "movewell_vision.v1",
  tools: [
    {
      name: "analyze_posture_frame",
      description: "Ingests raw 2D keypoint joint locations and calculates forward head tilt, thoracic kyphosis, and shoulder asymmetry.",
      inputSchema: {
        type: "object",
        properties: {
          keypoints: {
            type: "array",
            items: {
              type: "object",
              properties: {
                joint: { type: "string" },
                x: { type: "number" },
                y: { type: "number" },
                confidence: { type: "number" }
              },
              required: ["joint", "x", "y"]
            }
          }
        },
        required: ["keypoints"]
      }
    },
    {
      name: "get_lumbar_flexion_angle",
      description: "Calculates lumbar spine flexion angle during squats or bends to detect rounding.",
      inputSchema: {
        type: "object",
        properties: {
          hip_x: { type: "number" },
          hip_y: { type: "number" },
          shoulder_x: { type: "number" },
          shoulder_y: { type: "number" },
          knee_x: { type: "number" },
          knee_y: { type: "number" }
        },
        required: ["hip_x", "hip_y", "shoulder_x", "shoulder_y"]
      }
    },
    {
      name: "get_movement_balance_score",
      description: "Computes overall balance distribution score (0-100) across left and right lower body keypoints.",
      inputSchema: {
        type: "object",
        properties: {
          left_knee_angle: { type: "number" },
          right_knee_angle: { type: "number" }
        },
        required: ["left_knee_angle", "right_knee_angle"]
      }
    }
  ] as MCPToolDescriptor[]
};
