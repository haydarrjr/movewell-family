/**
 * Movewell Vision Service Entry Point.
 */
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import { MOVEWELL_VISION_MCP_CONTRACT } from "./mcpContract";

dotenv.config();

const app = express();
const PORT = process.env.VISION_PORT || 2091;

app.use(cors());
app.use(express.json());

// Health Check Endpoint
app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
    service: "Movewell Vision Service",
    version: "1.0.0",
    contract: MOVEWELL_VISION_MCP_CONTRACT.contractName
  });
});

// MCP Tools Registry Endpoint
app.get("/mcp/tools", (req, res) => {
  res.json({
    contract: MOVEWELL_VISION_MCP_CONTRACT.contractName,
    tools: MOVEWELL_VISION_MCP_CONTRACT.tools
  });
});

// MCP Tool Execution Endpoint
app.post("/mcp/execute", (req, res) => {
  const { tool_name, arguments: args } = req.body;

  if (tool_name === "analyze_posture_frame") {
    const keypoints = args?.keypoints || [];
    res.json({
      status: "success",
      result: {
        forward_head_angle: 12.4,
        thoracic_alignment: "good",
        shoulder_asymmetry_cm: 0.4,
        posture_score: 88,
        keypoints_processed: keypoints.length
      }
    });
    return;
  }

  if (tool_name === "get_lumbar_flexion_angle") {
    res.json({
      status: "success",
      result: {
        lumbar_flexion_deg: 178.5,
        spine_neutral: true,
        risk_flag: false
      }
    });
    return;
  }

  if (tool_name === "get_movement_balance_score") {
    res.json({
      status: "success",
      result: {
        balance_score: 94.2,
        weight_distribution: "49% L / 51% R"
      }
    });
    return;
  }

  res.status(404).json({ error: `Tool '${tool_name}' not found.` });
});

app.listen(PORT, () => {
  console.log(`[Movewell Vision] Service running on http://0.0.0.0:${PORT}`);
});
